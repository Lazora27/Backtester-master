import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'BradleySiderograph': 1.0
        })
    )
