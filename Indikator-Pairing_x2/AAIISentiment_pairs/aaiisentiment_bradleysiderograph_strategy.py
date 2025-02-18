import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'BradleySiderograph': 1.0
        })
    )
