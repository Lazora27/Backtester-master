import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
