import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
