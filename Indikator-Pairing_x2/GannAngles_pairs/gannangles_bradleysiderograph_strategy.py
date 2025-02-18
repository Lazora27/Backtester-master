import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'BradleySiderograph': 1.0
        })
    )
