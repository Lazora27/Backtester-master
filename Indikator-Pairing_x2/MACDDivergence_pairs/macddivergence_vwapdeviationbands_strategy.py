import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
