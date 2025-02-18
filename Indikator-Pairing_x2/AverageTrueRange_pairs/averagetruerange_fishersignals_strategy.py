import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'FisherSignals': 1.0
        })
    )
