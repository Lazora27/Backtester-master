import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
