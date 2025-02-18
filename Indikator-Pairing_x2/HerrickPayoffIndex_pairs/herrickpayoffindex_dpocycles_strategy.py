import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
