import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'BollingerBands': 1.0
        })
    )
