import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und FisherSignals
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'FisherSignals': 1.0
        })
    )
