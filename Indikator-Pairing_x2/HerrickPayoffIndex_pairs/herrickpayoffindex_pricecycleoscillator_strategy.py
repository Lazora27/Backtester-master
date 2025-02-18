import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
