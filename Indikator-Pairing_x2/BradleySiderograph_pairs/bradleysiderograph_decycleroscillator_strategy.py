import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
