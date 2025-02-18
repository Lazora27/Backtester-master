import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
