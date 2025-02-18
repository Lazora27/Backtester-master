import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
