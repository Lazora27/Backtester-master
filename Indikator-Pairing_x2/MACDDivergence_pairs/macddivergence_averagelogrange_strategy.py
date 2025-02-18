import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AverageLogRange': 1.0
        })
    )
