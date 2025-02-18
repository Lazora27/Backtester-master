import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'BradleySiderograph': 1.0
        })
    )
