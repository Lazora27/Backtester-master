import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'IntradayIntensity': 1.0
        })
    )
