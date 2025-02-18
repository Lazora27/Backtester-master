import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'BradleySiderograph': 1.0
        })
    )
