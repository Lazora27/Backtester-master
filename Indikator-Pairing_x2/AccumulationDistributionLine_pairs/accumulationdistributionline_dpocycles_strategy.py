import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'DPOCycles': 1.0
        })
    )
