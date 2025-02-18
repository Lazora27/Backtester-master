import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'BradleySiderograph': 1.0
        })
    )
