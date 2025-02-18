import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsAccumulationDistribution_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsAccumulationDistribution und DPOCycles
    """
    
    params = (
        ('indicators', {
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'WilliamsAccumulationDistribution': 1.0,
            'DPOCycles': 1.0
        })
    )
