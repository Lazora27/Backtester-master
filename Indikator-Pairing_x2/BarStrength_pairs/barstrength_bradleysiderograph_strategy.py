import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'BradleySiderograph': 1.0
        })
    )
