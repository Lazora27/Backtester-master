import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'DPOCycles': 1.0
        })
    )
