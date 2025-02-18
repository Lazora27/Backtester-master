import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
