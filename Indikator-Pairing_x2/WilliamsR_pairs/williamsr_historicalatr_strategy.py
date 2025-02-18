import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HistoricalATR': 1.0
        })
    )
