import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'DPOCycles': 1.0
        })
    )
