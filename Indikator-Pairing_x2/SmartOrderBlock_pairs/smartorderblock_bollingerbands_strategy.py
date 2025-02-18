import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und BollingerBands
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'BollingerBands': 1.0
        })
    )
