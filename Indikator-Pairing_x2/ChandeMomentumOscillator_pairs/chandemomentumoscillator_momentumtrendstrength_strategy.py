import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeMomentumOscillator_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeMomentumOscillator und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'ChandeMomentumOscillator': {
                'class': ChandeMomentumOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeMomentumOscillator'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'ChandeMomentumOscillator': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
