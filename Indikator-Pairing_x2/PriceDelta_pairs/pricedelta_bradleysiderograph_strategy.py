import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'BradleySiderograph': 1.0
        })
    )
