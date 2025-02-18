import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'HistoricalATR': 1.0
        })
    )
