import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'IntradayIntensity': 1.0
        })
    )
