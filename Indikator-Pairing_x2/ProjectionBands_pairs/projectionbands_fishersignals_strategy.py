import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'FisherSignals': 1.0
        })
    )
