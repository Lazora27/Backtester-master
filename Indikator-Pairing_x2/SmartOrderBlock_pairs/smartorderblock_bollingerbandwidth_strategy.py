import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
