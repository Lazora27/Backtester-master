import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und MassIndex
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'MassIndex': 1.0
        })
    )
