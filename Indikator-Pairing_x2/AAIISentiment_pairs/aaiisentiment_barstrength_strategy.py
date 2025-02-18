import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und BarStrength
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'BarStrength': 1.0
        })
    )
