import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
