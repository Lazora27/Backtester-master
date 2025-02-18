import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'IntradayIntensity': 1.0
        })
    )
