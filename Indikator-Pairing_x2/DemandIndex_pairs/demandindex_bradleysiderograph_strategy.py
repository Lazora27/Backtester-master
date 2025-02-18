import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
