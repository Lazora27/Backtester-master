import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
