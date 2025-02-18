import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'BradleySiderograph': 1.0
        })
    )
