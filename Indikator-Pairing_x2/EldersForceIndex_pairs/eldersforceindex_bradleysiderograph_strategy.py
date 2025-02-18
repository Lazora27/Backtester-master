import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
