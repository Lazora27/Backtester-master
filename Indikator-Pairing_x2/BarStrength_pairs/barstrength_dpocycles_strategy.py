import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und DPOCycles
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'DPOCycles': 1.0
        })
    )
