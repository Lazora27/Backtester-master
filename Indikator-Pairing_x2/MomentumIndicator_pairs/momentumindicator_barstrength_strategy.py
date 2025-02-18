import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und BarStrength
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'BarStrength': 1.0
        })
    )
