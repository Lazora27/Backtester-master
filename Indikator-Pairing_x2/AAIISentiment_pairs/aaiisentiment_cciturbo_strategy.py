import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'CCITurbo': 1.0
        })
    )
