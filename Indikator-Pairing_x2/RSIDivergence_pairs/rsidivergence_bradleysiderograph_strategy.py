import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'BradleySiderograph': 1.0
        })
    )
