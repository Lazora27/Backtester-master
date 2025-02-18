import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und PriceDelta
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'PriceDelta': 1.0
        })
    )
