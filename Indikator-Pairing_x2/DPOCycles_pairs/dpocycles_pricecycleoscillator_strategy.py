import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
