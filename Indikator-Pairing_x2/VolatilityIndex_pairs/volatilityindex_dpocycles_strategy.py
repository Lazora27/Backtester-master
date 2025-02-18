import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
