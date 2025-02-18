import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und DPOCycles
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'DPOCycles': 1.0
        })
    )
