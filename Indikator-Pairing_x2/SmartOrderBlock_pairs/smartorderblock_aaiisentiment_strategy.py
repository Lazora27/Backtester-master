import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AAIISentiment': 1.0
        })
    )
