import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
