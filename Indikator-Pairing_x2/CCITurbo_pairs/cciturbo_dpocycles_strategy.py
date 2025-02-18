import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'DPOCycles': 1.0
        })
    )
