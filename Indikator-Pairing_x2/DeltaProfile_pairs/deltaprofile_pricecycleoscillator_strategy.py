import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
