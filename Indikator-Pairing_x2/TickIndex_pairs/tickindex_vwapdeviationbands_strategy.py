import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
